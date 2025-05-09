import { Outlet } from "react-router-dom"

const Layout = () => {

    return (
        <div className="wrapper">
            <div className="top-bar"></div>
            <div className="container">
                <Outlet />
            </div>
        </div>
    )
}

export default Layout