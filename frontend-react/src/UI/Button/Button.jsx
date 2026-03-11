import React from "react";
import styles from "./Button.module.scss";

const Button = ({ children, variant = "primary", onClick, className }) => {
  const buttonClass = `
    ${styles.button}
    ${variant === "primary" ? styles.primary : ""}
    ${variant === "outline" ? styles.outline : ""}
    ${className || ""}
  `;

  return (
    <button className={buttonClass} onClick={onClick}>
      {children}
    </button>
  );
};

export default Button;