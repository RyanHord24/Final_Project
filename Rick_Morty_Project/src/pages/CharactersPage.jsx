import axios from 'axios'
import { useState, useEffect } from "react";
import CharacterCard from '/Users/miyapollard/Desktop/Rick_Morty_Project/src/components/CharacterCard.jsx';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useOutletContext } from "react-router-dom";
import Button from "react-bootstrap/Button";

function CharactersPage() {
    const[characters, setCharacters] = useState([]);
    const { favorites, setFavorites } = useOutletContext();
    const [currentPage, setCurrentPage] = useState(1);

    const getCharacters = async () => {
        let { data } = await axios.get(`https://rickandmortyapi.com/api/character/?page=${currentPage}`);
        setCharacters(data.results);
    }

    const setPage = () =>{
        return setCurrentPage(currentPage + 1);
    }
    useEffect(()=>{
        getCharacters();
      }, []);

    useEffect(()=>{
        setPage();
    }, getCharacters());

    return (
        <>
        <h1 className="flex justify-center items-center text-4xl">Rick and Morty Characters</h1>
        <ul className="flex flex-wrap">
        {characters.map((character) => (
          <CharacterCard
            key={character.id}
            ind={character}
            favorites={favorites}
            setFavorites={setFavorites}/>
            ))}
        </ul>
        <Button onClick={() => {
            setPage()
            }}>
        View next page
        </Button>
    </>
    )
}

export default CharactersPage;