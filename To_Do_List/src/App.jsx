import './App.css'

function App() {
  let count = 1
  const new_item = (evt) =>{
    let itemContainer = document.createElement("div")
    itemContainer.id = "itemContainerId"
    itemContainer.className = "itemContainerId"

    let input = document.createElement("p")
    input.innerHTML = `${count}. ${evt}`
    input.id = "inputId"

    let checkbox = document.createElement("input")
    checkbox.type = "checkbox"
    checkbox.id = "checkboxId"

    // let deleteButton = document.createElement("button")
    
    itemContainer.appendChild(checkbox)
    itemContainer.appendChild(input)

    document.getElementById('items').appendChild(itemContainer)
  }  

  const handleSubmit = async(evt) => {
    evt.preventDefault()
    let input = document.getElementById('user-input')
    let usrInput = input.value
    new_item(usrInput)
    input.value = ''
    count++
  }

  return (
    <>
      <h1>To-Do List</h1>
      <form onSubmit={(evt)=>handleSubmit(evt)}>
        <input id='user-input' type="text" placeholder='Enter New Task'/>
        <input type='submit'/>
        <p id='New Task'></p>
        <div id='items'></div>
      </form>
      {/* <input type="checkbox"/> */}
      {/* <div id='itemsContainer'></div> */}

    </>
  )
}

export default App
