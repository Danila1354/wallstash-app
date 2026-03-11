import styles from "./Header.module.scss";
import SearchInput from "../../UI/SearchInput/SearchInput.jsx";
import Button from "../../UI/Button/Button.jsx";

const Header = () => {
    return (
        <header className={styles.header}>
            <div className="container">
                <div className={styles.headerInner}>
                    <a className={styles.logo}>
                        <img src="/logo.png" alt=""/>
                        <span className={styles.logoText}>WallStash</span>
                    </a>
                    <SearchInput/>
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