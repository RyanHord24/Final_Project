import axios from "axios";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

const CharacterDetailsPage = () => {
    const [selected, setSelected] = useState(null);
    const { id } = useParams();

    const getCharacterInfo = async () =>{
        let { data } = await axios.get(`https://rickandmortyapi.com/api/character/${id}`)
        setSelected(data)
    }

    useEffect(() => {
        getCharacterInfo();
      }, []);

    return (
    <>
        {selected ? (
            <>
              <h1>{selected.name}</h1>
              <img src={selected.image} />
            </>
          ) : null}
    </>
    );
};

export default CharacterDetailsPage