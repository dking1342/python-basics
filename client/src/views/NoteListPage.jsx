import React, { useEffect, useState, useCallback } from 'react'
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
                    mode:"cors",
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
            <div>
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
            </div>
        )
    } 
    return (
        <div>no list</div>
    )

}

export default NoteListPage
