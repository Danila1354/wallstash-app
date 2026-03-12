import React from 'react';
import styles from './SectionHeader.module.scss';

const SectionHeader = ({ title, linkText, linkHref }) => {
  return (
    <div className={styles.header}>
      <h2 className={styles.title}>{title}</h2>

      {linkText && (
        <a href={linkHref} className={styles.link}>
          {linkText}
        </a>
      )}
    </div>
  );
};


export default SectionHeader;