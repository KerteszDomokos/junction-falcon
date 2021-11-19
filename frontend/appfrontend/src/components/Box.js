import React, { useState } from "react";
import "../Styling/Box.css";
import Draggable from "react-draggable";

let szamozas = 1;

function Box(props) {
  const [statt, setStatt] = useState(true);

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
                <span class="dot1"></span>
                <span class="dot2"></span>
              </div>
            </div>
          </Draggable>
        ))}
      </div>
    </React.Fragment>
  );
}

export default Box;
