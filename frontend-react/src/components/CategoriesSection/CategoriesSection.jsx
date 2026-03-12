import React from 'react';
import styles from './CategoriesSection.module.scss';
import SectionHeader from "../../UI/SectionHeader/SectionHeader.jsx";
import CategoryCard from "./CategoryCard/CategoryCard.jsx";
import NatureIcon from "@/assets/icons/nature.svg?component";

const CategoriesSection = () => {
    return (
        <div className={styles.section}>
            <div className="container">
                <SectionHeader
                  title="Browse Categories"
                  linkText="View all"
                  linkHref="/categories"
                />
                <CategoryCard title="Nature" icon={NatureIcon}/>
            </div>
        </div>
    );
};

export default CategoriesSection;