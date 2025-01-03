console.log("hello I'm connected")

const getImg = (imgSrc) => {
  let imgContainer = document.querySelector("#container")
  let img = document.createElement('img')
  img.src = imgSrc
  img.style.width = '25vmin'
  img.style.height = '25vmin'
  img.style.border = 'solid 1px black'
  imgContainer.appendChild(img)
}

// create a function
const getPokemonFrontDefault = () =>{
  // generate a random number between 1 and 1000
  let num = Math.floor(Math.random()*1000)
  // fetch pokemon data corresponding to rand int
  fetch(`https://random-d.uk/api`) // generates promise
    .then((response)=> response.json()) // turn response into json data generates promise
      .then((data)=>{
        // iterate through response to grab front_default sprite
        let front_default = 'https://random-d.uk/api/images/51.jpg'
        // return front_default sprite 
        getImg(front_default)
      })
      .catch((err)=>{
        alert("something went wrong")
      })
}

const getRickSanchez = async() => {
  try{
    const response = await fetch("https://rickandmortyapi.com/api/character/1")
    const data = await response.json()
    getPokemonImg(data.image)
  }
  catch(err){
    
  }
}