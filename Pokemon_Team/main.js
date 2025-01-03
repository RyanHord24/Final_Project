
const getPokemonImg = (imgSrc) => {
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
    let defaultType = ""
    // generate a random number between 1 and 1000
    let num = Math.floor(Math.random()*152)
    // fetch pokemon data corresponding to rand int
    fetch(`https://pokeapi.co/api/v2/pokemon/${num}`) // generates promise
      .then((response)=> response.json()) // turn response into json data generates promise
        .then((data)=>{
          // iterate through response to grab front_default sprite
          let front_default = data.sprites.front_default
          defaultType = data.types[0].type.name
          console.log(defaultType)
          // return front_default sprite 
          getPokemonImg(front_default)
          //getPokemonTeam(defaultType);
        })
        .catch((err)=>{
          alert("something went wrong")
        })
  }

  const getPokemonTeam = (defaultType) =>{
    count = 0
    while(count < 5){
        let num = Math.floor(Math.random()*152)
        fetch(`https://pokeapi.co/api/v2/pokemon/${num}`)
          .then((response)=> response.json())
            .then((data)=>{
                if(data.types[0].type.name === defaultType){
                    let front_default = data.sprites.front_default
                    getPokemonImg(front_default)
                    count++
                }
            })
        } 
  }