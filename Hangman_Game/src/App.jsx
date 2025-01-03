import { useState } from 'react'
import './App.css'
import words from './data/words.json'
function App() {
  const [displayWord, setdisplayWord] = useState(null);
  const [userGuess, setuserGuess] = useState("")
  const [answer] = useState(words[Math.floor(Math.random() * words.length + 1)])

  const generateWord = ()=>{
    let hidden_word = answer.split("").map((ltr) => "_");
    let hidden_word_tag = hidden_word.join(" ");
    return setdisplayWord(hidden_word_tag)
  }

  const checkGuessedLetter = (e)=>{
    e.preventDefault()
    guessLetter()
  }

  const guessLetter = ()=>{
    let hidden_word = displayWord.split(" ")
    //console.log(hidden_word)
    for(let i = 0; i < answer.length; i++){
      if(userGuess === answer[i]){
        hidden_word[i] = userGuess
        let hidden_word_tag = hidden_word.join(" ");
        return setdisplayWord(hidden_word_tag)
      }
    }
    return displayWord 
  }

  return (
    <>
      <h1>Hangman Game</h1>
      <button onClick={generateWord}>Start Game</button>
      <p id='displayWord'>{displayWord}</p>
      <form onSubmit={(evt)=>checkGuessedLetter(evt)}>
        <input id='user-input' type="text" maxLength={1} value={userGuess} placeholder='Guess a Letter'
          onChange={(e) => setuserGuess(e.target.value)}/>
        <input type='submit'/>
      </form>
    </>
  )
}


export default App
