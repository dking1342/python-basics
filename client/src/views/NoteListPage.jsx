import React, { useEffect, useState } from 'react'

const NoteListPage = () => {
    let [notes,setNotes] = useState([]);
    let [errors,setErrors] = useState("");
    let [loading, setLoading] = useState(false);
    
    
    let getNotes = async () => {
        setLoading(true);
        try {
            let response = await fetch("http://localhost:8000/api/notes/",{
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
    }

    useEffect(() => {
        getNotes()
    }, [])


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
                {
                    notes.map(note=>(
                        <div key={note.id} >{note.body}</div>
                    ))
                }
            </div>
        )
    } 
    return (
        <div>no list</div>
    )

}

export default NoteListPage
