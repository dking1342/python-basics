import React, { useCallback, useEffect, useState } from 'react'

const NotePage = ({ match, history }) => {
    const id = match.params.id;
    const [note,setNote] = useState(null);
    const [errors,setErrors] = useState("");
    const [loading, setLoading] = useState(false);

    let cookies = document.cookie;
    let csrfToken = cookies.split("=")[1]

    const updateNote = async () => {
        setLoading(true);
        try {
            const updateResponse = await fetch(`/api/notes/${id}/update/`,{
                method:"PUT",
                headers:{
                    "X-CSRFToken":csrfToken,
                    "Content-Type":"application/json"
                },
                body:JSON.stringify(note)
            })
            let updateData = await updateResponse.json()
            setNote(updateData)
        } catch (error) {
            setErrors(error.message)
        }
        setLoading(false)
        history.push("/")
    }

    const deleteNote = async () => {
        if(window.confirm("Are you sure you want to delete?")){
            setLoading(true);
            try {
                const deleteResponse = await fetch(`/api/notes/${id}/delete/`,{
                    method:"DELETE",
                    headers:{
                        "X-CSRFToken":csrfToken,
                        "Content-Type":"application/json"
                    },
                    body:null
                })
                const deleteData = await deleteResponse.json();
                setNote(deleteData);
            } catch (error) {
                setErrors(error.message)
            }
            setLoading(false);
            history.push("/")
        }
    }

    const createNote = async () => {
        setLoading(true);
        try {
            const createResponse = await fetch(`/api/notes/create/`,{
                method:"POST",
                headers:{
                    "X-CSRFToken":csrfToken,
                    "Content-Type":"application/json"
                },
                body:JSON.stringify(note)
            })
            let createData = await createResponse.json()
            setNote(createData)
        } catch (error) {
            setErrors(error.message)
        }
        setLoading(false)
        history.push("/")
    }

    const getNote = useCallback(async () => {
            if(id === "new"){
                setNote("new note")
            } else {
                setLoading(true);
                try {
                    let response = await fetch(`/api/notes/${id}`,{
                        method:"GET",
                        headers:{
                            "Content-Type":"application/json"
                        },
                        body:null,
                    });
                    let data = await response.json();
                    setNote(data)
                } catch (error) {
                    console.log("error",error.message)
                    setErrors(error.message)
                }
                setLoading(false);
            }
        },
        [id],
    )

    const handleDelete = () => {
        deleteNote()
    }

    const handleSubmit = () => {
        if(note.body && id !== "new"){
            updateNote()
        } 
        if(note.body && id === "new"){
            createNote()
        }
        if(!note.body && id !== "new"){
            deleteNote()
        }
        if(!note.body && id === "new"){
            history.push("/")
        }
    }

    useEffect(()=>{
        getNote()
    },[getNote])

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
    if(!loading && note){
        return(
            <div className="note">
                <div className="note-header">
                    <button onClick={ handleSubmit } >&#x2039;</button>
                </div>
                <textarea onChange={(e)=> { setNote({...note,"body":e.target.value})}} defaultValue={ note.body }></textarea>
                <button onClick={ handleDelete } className="floating-button">&#x2715;</button>
            </div>
        )
    }
    return (
        <div>no note</div>
    )
}

export default NotePage
