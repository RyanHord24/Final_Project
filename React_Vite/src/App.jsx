import './App.css'
//import axios from 'axios'

function App() {
  let count = 0;
  let team = ""

  const getPokemonImg = (url) =>{
    let img = document.createElement("img")
    img.src = url
    img.className = 'pokemon-img'
    document.getElementById('img-container').appendChild(img)
  }

    const getPokemonType = (type) =>{
      let desc_type = document.createElement("p")
      desc_type.innerHTML = `Type: ${type.charAt(0).toUpperCase() + type.substring(1).toLowerCase()}`
      document.getElementById('img-container').appendChild(desc_type)
    }

    const getPokemonName = (pokemon_name) =>{
      let desc_name = document.createElement("p")
      desc_name.innerHTML = `Name: ${pokemon_name.charAt(0).toUpperCase() + pokemon_name.substring(1).toLowerCase()}`
      document.getElementById('img-container').appendChild(desc_name)
    }  


  const getPokemon = () =>{
    if(count === 0){
    let num = Math.floor(Math.random()*152)
    fetch(`https://pokeapi.co/api/v2/pokemon/${num}`)
      .then((response)=> response.json())
        .then((data)=>{
          let front_default = data.sprites.front_default
          let type = data.types[0].type.name
          let pokemon_name = data.name
          getPokemonImg(front_default)
          getPokemonType(type)
          getPokemonName(pokemon_name)
        })
      count++
      team = type
    }
  }

  return (
    <>
      <h1>Pokemon Team Generator</h1>
      <h3>Click the "Generate Team" button 6 times. The first Pokemon will be a random type. After that, they will all match the first Pokemon.</h3>
      <div id='img-container' className='img-container'>
      </div>
      <br></br>
      <p id='PokemonType'></p>
      <div>
        <button onClick={getPokemon}>Generate Team</button>
      </div>
    </>
  )

}
  



export default App
