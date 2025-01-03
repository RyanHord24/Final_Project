import { useOutletContext } from "react-router-dom";
import CharacterCard from "/Users/miyapollard/Desktop/Rick_Morty_Project/src/components/CharacterCard.jsx";

const FavoritesPage = () => {
    const { favorites, setFavorites } = useOutletContext();

    return (
        <>
          <h2>Favorite Characters Page</h2>
          {favorites ? (
            favorites.map((character) => (
              <CharacterCard
                key={character.id}
                ind={character}
                setFavorites={setFavorites}
                favorites={favorites}
              />
            ))
          ) : (
            <h3>No Characters Selected</h3>
          )}
        </>
      );
    };
    
export default FavoritesPage;