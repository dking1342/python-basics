import React from 'react'
import { Link } from 'react-router-dom'

const AddButton = () => {
    return (
        <Link to="/note/new" className="floating-button">
            &#x271A;
        </Link>
    )
}

export default AddButton
