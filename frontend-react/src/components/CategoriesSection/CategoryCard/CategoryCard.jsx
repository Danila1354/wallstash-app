import React from 'react';
import styles from './CategoryCard.module.scss';

const CategoryCard = ({ icon, title }) => {
  return (
    <div className={styles.card}>
      <div className={styles.icon}>
        {icon}
      </div>

      <span className={styles.title}>
        {title}
      </span>
    </div>
  );
};

export default CategoryCard;