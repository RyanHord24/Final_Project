import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import { useNavigate } from "react-router-dom";

export default function CharacterCard({ ind, setFavorites, favorites }) {
  const navigate = useNavigate();

  return (
    <Card style={{ width: "18rem" }}>
      <Card.Img variant="top" src={ind.image} />
      <Card.Body>
        <Card.Title>{ind.name}</Card.Title>
        <Button variant="primary" onClick={() => navigate(`/CharacterDetailsPage/${ind.id}/`)}>
          Get Details
        </Button>
        <Button variant="warning" onClick={()=> setFavorites([...favorites, ind])}>
          Add to favorites
        </Button>
      </Card.Body>
    </Card>
  );
}