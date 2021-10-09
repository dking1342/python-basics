import React, { useCallback, useEffect, useState } from 'react'
import { Link } from 'react-router-dom';

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

    const handleSubmit = () => {
        updateNote()
    }

    const getNote = useCallback(async () => {
            setLoading(true);
            try {
                let response = await fetch(`/api/notes/${id}`,{
                    method:"GET",
                    mode:"cors",
                    headers:{
                        "Content-Type":"application/json"
                    },
                    body:null,
                });
                let data = await response.json();
                setNote(data)
            } catch (error) {
                setErrors(error.message)
            }
            setLoading(false);
        },
        [id],
    )

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
                    <h3>
                        <Link to="/">&#x2039;</Link>
                    </h3>
                    <button onClick={ handleSubmit }>Update</button>
                </div>
                <textarea onChange={(e)=> { setNote({...note,"body":e.target.value})}} defaultValue={ note.body }></textarea>
            </div>
        )
    }
    return (
        <div>no note</div>
    )
}

export default NotePage
