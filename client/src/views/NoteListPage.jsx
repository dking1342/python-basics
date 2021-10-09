import React, { useEffect, useState, useCallback } from 'react'
import AddButton from '../components/AddButton';
import ListItem from '../components/ListItem'

const NoteListPage = () => {
    let [notes,setNotes] = useState([]);
    let [errors,setErrors] = useState("");
    let [loading, setLoading] = useState(false);
    
    let getNotes = useCallback(async() => {
            setLoading(true);
            try {
                let response = await fetch("/api/notes/",{
                    method:"GET",
                    headers:{
                        "Content-Type":"application/json"
                    },
                    body:null,
                });
                let data = await response.json();
                setNotes(data)
            } catch (error) {
                setErrors(error.message)
            }
            setLoading(false);
        },
        [],
    )

    useEffect(() => {
        getNotes()
    }, [getNotes])


    if(loading){
        return(
            <div>loading...</div>
        )
    }
    if(!loading && errors){
        return(
            <div>{ errors }</div>
        )
    }  
    if (!loading && notes.length){
        return (
            <div className="notes">
                <div className="notes-header">
                    <h2 className="notes-title">&#9782; Notes</h2>
                    <p className="notes-count">{ notes.length }</p>
                </div>
                <div className="notes-list">
                    {
                        notes.map((note,index)=>(
                            <ListItem 
                                key={ note.id }
                                note={ note }
                            />
                        ))
                    }
                </div>
                <AddButton />
            </div>
        )
    } 
    return (
        <div>no list</div>
    )

}

export default NoteListPage
