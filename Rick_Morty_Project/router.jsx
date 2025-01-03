// router.jsx
import { createBrowserRouter } from "react-router-dom";
import App from "/Users/miyapollard/Desktop/Rick_Morty_Project/src/App.jsx";
import HomePage from "/Users/miyapollard/Desktop/Rick_Morty_Project/src/pages/HomePage.jsx";
import AboutPage from "/Users/miyapollard/Desktop/Rick_Morty_Project/src/pages/AboutPage.jsx";
import CharactersPage from "/Users/miyapollard/Desktop/Rick_Morty_Project/src/pages/CharactersPage.jsx"
import CharacterDetailsPage from "/Users/miyapollard/Desktop/Rick_Morty_Project/src/pages/CharacterDetailsPage.jsx"
import FavoritesPage from "/Users/miyapollard/Desktop/Rick_Morty_Project/src/pages/FavoritesPage.jsx"

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      {
        index: true,
        element: <HomePage />,
      },
      {
        path: "AboutPage",
        element: <AboutPage />,
      },
      {
        path: "CharactersPage",
        element: <CharactersPage />,
      },
      {
        path: "CharacterDetailsPage/:id/",
        element: <CharacterDetailsPage />,
    },
    {
        path: "FavoritesPage",
        element: <FavoritesPage />,
      },
    ],
  },
]);

export default router;