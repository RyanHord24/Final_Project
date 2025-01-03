// import NavBar from "../components/NavBar.jsx"
import axios from "axios";
import React from 'react';
import NotebookCard from "../src/components/NotebookCard.jsx";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const NotebookPage = () => {
    const [notebooks, setNotebooks] = useState([]);
    const navigate = useNavigate();
    const [isAuthenticated, setIsAuthenticated] = useState(false);

    useEffect(() => {
        const token = localStorage.getItem("authToken");
        if (token) {
            setIsAuthenticated(true);
        } else {
            alert("You must be logged in to access this page.");
            navigate("/");
        }
    }, [navigate]);

    useEffect(() => {
        const fetchNotebooks = async () => {
            const authToken = localStorage.getItem("authToken");
            try {
                const response = await axios.get('http://localhost:8000/api/v1/notebook/country/', {
                    headers: {
                        Authorization: `Token ${authToken}`,
                    },
                });
                setNotebooks(response.data);
            } catch (error) {
                console.error("Error fetching favorites:", error);
            }
        };

        fetchNotebooks();
    }, []);

    const handleUpdate = (updatedNotebook) => {
        setNotebooks((prevNotebooks) =>
            prevNotebooks.map((notebook) =>
                notebook.id === updatedNotebook.id ? updatedNotebook : notebook
            )
        );
    };

    const handleDelete = (deletedNotebookId) => {
        setNotebooks((prevNotebooks) =>
            prevNotebooks.filter((notebook) => notebook.id !== deletedNotebookId)
        );
    };



    return (
        <>
        <NavBar />
        <h1 className="pl-2">Notebooks</h1>
        <h3 className="pl-2">This page contains the notebooks that you created for your favorite countries. Here you can insert information like the flights and hotels you have booked, as well as your plans and reservations while on your trips.</h3>
        <div className="favorite-list">
        <ul style={{
                display: "flex", 
                flexWrap: "wrap", 
                gap: "1rem", 
                justifyContent: "center"
                }}>
                {notebooks.map((notebook) => (
                    <NotebookCard key={notebook.id} notebook={notebook} onUpdate={handleUpdate} onDelete={handleDelete} />
                ))}
        </ul>
        </div>
        </>
    )
 }

export default NotebookPage;