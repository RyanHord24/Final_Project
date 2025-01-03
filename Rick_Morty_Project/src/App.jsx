import { Outlet } from "react-router-dom";
import { Link } from "react-router-dom";
import NavBar from "/Users/miyapollard/Desktop/Rick_Morty_Project/src/NavBar.jsx"
import { useState, useEffect } from "react";

export default function App() {
  const [favorites, setFavorites] = useState([])

  useEffect(()=>{
    console.log(favorites)
  }, [favorites])

  return(
  <> 
  <NavBar />
  <Outlet context={{favorites, setFavorites}}/>
  </>
  )
}

