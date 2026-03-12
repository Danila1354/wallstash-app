import React from 'react';
import styles from './HeroSection.module.scss';

const HeroSection = () => {
    return (
        <div className={styles.hero}>
            <div className="container">
                <div className={styles.heroText}>
                    <h1 className={styles.heroTitle}>Discover Stunning Wallpapers</h1>
                    <p className={styles.heroSubtitle}>Explore millions of high-quality wallpapers for your desktop and mobile</p>
                </div>
                <div className={styles.heroImageContainer}>
                    <img src="/hero-example.jpg" alt=""/>
                </div>
            </div>
        </div>
    );
};

export default HeroSection;