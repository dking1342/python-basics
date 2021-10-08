import React from 'react'
import { BrowserRouter as Router, Route } from 'react-router-dom'
import Header from './components/Header'
import NoteListPage from './views/NoteListPage'
import NotePage from './views/NotePage'

const App = () => {
  return (
    <Router>
      <div className="App">
          <Header />
          <Route path="/" exact component={ NoteListPage } />
          <Route path="/note/:id" component={ NotePage } />
      </div>
    </Router>
  )
}

export default App
