import React, { useCallback, useEffect, useState } from 'react'

const NotePage = ({ match }) => {
    const id = match.params.id;
    const [note,setNote] = useState(null);
    const [errors,setErrors] = useState("");
    const [loading, setLoading] = useState(false);

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
            <div>{ note.body }</div>
        )
    }
    return (
        <div>no note</div>
    )
}

export default NotePage
