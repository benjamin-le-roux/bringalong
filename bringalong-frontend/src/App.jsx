import { Route, Routes } from 'react-router-dom'
import Layout from './pages/Layout'
import List from './pages/Layout'
import './App.css'

const App = () => {


  return (
    <Routes>
      <Route path='/' element={<Layout/>}>
        <Route index element={<List />}></Route>
      </Route>
    </Routes>
  )
}

export default App
