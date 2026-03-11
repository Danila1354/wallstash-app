import React from "react";
import styles from "./SearchInput.module.scss";
import { Search } from "lucide-react"; // иконка

const SearchInput = () => {
  return (
    <div className={styles.wrapper}>
      <Search className={styles.icon} size={18} />
      <input
        className={styles.searchInput}
        placeholder="Search wallpapers..."
      />
    </div>
  );
};

export default SearchInput;