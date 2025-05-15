import React from "react";
import logo from "./logo.png";

export function Footer() {
  return (
    <img
      style={{
        position: "absolute",
        maxWidth: "500px",
        bottom: "50px",
        right: "50px",
      }}
      src={logo}
    />
  );
}
