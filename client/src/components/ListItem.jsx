import React from 'react'
import { Link } from 'react-router-dom'

const ListItem = ({ note }) => {
    return (
        <Link to={`/note/${note.id}`}>
            <div className="notes-list-item">
                <h3>{ note.body.slice(0,35) }</h3>
                <p>{ note.body.slice(35,70) }</p>
                <p>{ new Date(note.updated).toDateString() }</p>
            </div>
        </Link>
    )
}

export default ListItem
