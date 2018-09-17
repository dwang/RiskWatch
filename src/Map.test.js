import React from "react";
import ReactDOM from "react-dom";
import MapContainer from "./Map";

it("renders without crashing", () => {
  const div = document.createElement("div");
  ReactDOM.render(<MapContainer />, div);
  ReactDOM.unmountComponentAtNode(div);
});
