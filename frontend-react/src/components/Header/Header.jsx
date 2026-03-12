import styles from "./Header.module.scss";
import SearchInput from "../../UI/SearchInput/SearchInput.jsx";
import Button from "../../UI/Button/Button.jsx";
import { NavLink } from "react-router-dom";

const Header = () => {
  return (
    <header className={styles.header}>
      <div className="container">
        <div className={styles.headerInner}>

          <NavLink to="/" className={styles.logo}>
            <img src="/logo.png" alt="" />
            <span className={styles.logoText}>WallStash</span>
          </NavLink>

          <nav className={styles.nav}>
            <NavLink to="/gallery" className={styles.navLink}>
              Gallery
            </NavLink>

            <NavLink to="/categories" className={styles.navLink}>
              Categories
            </NavLink>
          </nav>

          <SearchInput />

          <div className={styles.buttons}>
            <Button variant="outline">Log In</Button>
            <Button variant="primary">Register</Button>
          </div>

        </div>
      </div>
    </header>
  );
};

export default Header;