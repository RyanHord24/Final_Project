import { useState, useEffect } from 'react'
import './App.css'
import axios from 'axios'
import Form from 'react-bootstrap/Form'

function App() {
  let count = 0
  let shiny_click_count = 0

  const[selectedPokemon, setselectedPokemon] = useState(null)
  const[usrInput, setusrInput] = useState("")
  
  const getPokemonInfo = async ()=> {
    const { data } = await axios.get(`https://pokeapi.co/api/v2/pokemon/${usrInput}`);
    console.log(data)
    console.log(data.sprites.front_default)
    console.log(data.sprites.front_shiny)
    console.log(data.abilities)
    console.log(data.types)
    console.log(data.cries)
    setusrInput("")
    if(count > 0){
      deletePokemonImg()
    }
    setselectedPokemon(data);
    getPokemonImg(data)
  }; 

  const defaultPokemonInfo = (e)=> {
    e.preventDefault();
    getPokemonInfo()
    let ability_description = document.getElementById('description');
    ability_description.innerHTML = null

    count++
  }

  const deletePokemonImg = () => {
    let img = document.getElementById(`pokemon-img-${count}`)
    if (img) {
      img.remove();
    }
    if(document.getElementById(`pokemon-img-${count}`) === null){
      let img = document.getElementById('pokemon-shiny');
        if (img) {
          img.remove();
        }
    }
  }

  const getPokemonImg = (data) => {
    if (count > 1) {
      deletePokemonImg();
    }
      let img = document.createElement("img") //<img src='#'/>
      img.src = data.sprites.front_default
      img.id = `pokemon-img-${count}`
      img.className = "size-40"
      document.getElementById('main-display').appendChild(img)
    }

  const getShiny = () => {
    shiny_click_count++
    if(shiny_click_count % 2 != 0){
    let parent_element = document.getElementById('main-display')
    let old_child = document.getElementById(`pokemon-img-${count + 1}`)
    let shinyImg = document.createElement("img")
    shinyImg.src = selectedPokemon.sprites.front_shiny
    shinyImg.id = 'pokemon-shiny'
    shinyImg.className = "size-40"
    return parent_element.replaceChild(shinyImg, old_child)
    }
    else if(shiny_click_count % 2 === 0){
      let parent_element = document.getElementById('main-display')
      let shiny_mon = document.getElementById('pokemon-shiny')
      let old_child = document.createElement("img")
      old_child.src = selectedPokemon.sprites.front_default
      old_child.id = `pokemon-img-${count + 1}`
      old_child.className = "size-40"
      return parent_element.replaceChild(old_child, shiny_mon)
    }
  }

  const getAbility = () => {
    let ability_list = [];
    let ability_description = document.getElementById('description');
    for(let i = 0; i < selectedPokemon.abilities.length; i++){
      ability_list.push(selectedPokemon.abilities[i].ability.name)
    }
    return ability_description.innerHTML = (ability_list.join(" and "))
  }

  const getType = () => {
    let type_list = [];
    let pokemon_type = document.getElementById('description');
    for(let i = 0; i < selectedPokemon.types.length; i++){
      type_list.push(selectedPokemon.types[i].type.name)
    }
    return pokemon_type.innerHTML = (type_list.join(" and "))
  }

  const getPokemonCry = () => {
    let audio = document.createElement("audio");
    audio.src = selectedPokemon.cries.latest;
    audio.type = "audio/ogg";
    audio.id = `pokemon-audio-${count}`;
    audio.autoplay = true
  }

  return (
    <>
    <div
    className="min-h-screen pl-20 pr-20"
    style={{
        backgroundImage: `url('https://i.pinimg.com/736x/39/3c/e6/393ce636c6ceac0b15ad4c454f247d60.jpg')`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
    }}>
      {/* <h1 className="text-3xl font-bold underline">
      Bootleg Pokedex: $10 to look up a Pokemon
    </h1> */}
    <img src='https://archives.bulbagarden.net/media/upload/4/4b/Pok%C3%A9dex_logo.png' className="mx-auto"></img>
    <Form onSubmit={(e) => defaultPokemonInfo(e)}>
      <Form.Control
        className= 'border-solid border-8 border-grey-600 m-4'
        type="text"
        value={usrInput}
        onChange={(e) => setusrInput(e.target.value)}
      />
        <button className= 'border-solid border-2 ' type="submit" placeholder="What Pokemon Would you like info on?">Submit</button>
    </Form>
    <div className= 'p-3 rounded-3xl h-130 w-70 border-solid border-4 border-black ml-75 mr-75 bg-red-500' id='container'>
      <div id='visual-container'>
        <div id='main-display' className='border-solid border-2 border-black rounded-xl ml-80 mr-80 mb-2 bg-cyan-100 h-60 border-solid border-8 border-red-500 flex justify-center items-center pt-12 flex-wrap'></div>
        <div id='description' className='border-2 border-black rounded-xl ml-80 mr-80 mb-2 bg-lime-500 h-40 border-solid border-8 border-red-500 p-12'></div>
      </div>
      <div id='mini-container' className='bg-red-500'></div>
        <div className="flex justify-center items-center space-x-4 bg-red-500">
          <div className='rounded-xl border-2 border-black w-20 border-solid border-4 border-blue-300 bg-blue-300'><button onClick={getShiny}>Shiny</button></div>
          <div className='rounded-xl border-2 border-black w-20 border-solid border-4 border-blue-300 bg-blue-300'><button onClick={getAbility}>Abilities</button></div>
          <div className='rounded-xl border-2 border-black w-20 border-solid border-4 border-blue-300 bg-blue-300'><button onClick={getType}>Types</button></div>
          <div className='rounded-xl border-2 border-black w-20 border-solid border-4 border-blue-300 bg-blue-300'><button onClick={getPokemonCry}>Cries</button></div>
        </div>
    </div>
    </div>
    </>
  )
}

export default App
