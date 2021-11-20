import React, { useState } from "react";
import "../Styling/Box.css";
import Draggable from "react-draggable";
import LineTo from "react-lineto";

let szamozas = 1;

function Box(props) {
  const [statt, setStatt] = useState(true);
  const [parameters, setParameters] = useState([]);

  const kattintas = (event) => {
    if (statt) {
      event.preventDefault();
      const item2 = {
        xkoord: event.clientX,
        ykoord: event.clientY,
        szamozas: szamozas,
      };
      props.setItemek((oldArray) => [...oldArray, item2]);
      szamozas++;
      setStatt(true);
    }
    console.log(statt);
  };
  const draggingprocess = () => {
    setStatt(false);
  };
  const draggingends = () => {
    setStatt(true);
  };
  const clickedondot = () => {
    console.log("Fuck");
  };
  return (
    <React.Fragment>
      <div className="drawing-area" onClick={kattintas}>
        {props.itemek.map((item) => (
          <Draggable onStart={draggingprocess} onStop={draggingends}>
            <div
              draggable
              className="dots"
              style={{ top: item.ykoord + "px", left: item.xkoord + "px" }}
              key={item.szamozas}
              draggable="true"
            >
              <div className="circle">
                <span className="dot1" onClick={clickedondot}></span>
                <span className="dot2" onClick={clickedondot}></span>
              </div>
            </div>
          </Draggable>
        ))}
      </div>
    </React.Fragment>
  );
}

export default Box;
