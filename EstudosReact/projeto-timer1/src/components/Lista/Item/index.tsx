import React from "react"
import Style from "./Lista.module.scss";
export default function Item(props: {tarefa: string, tempo: string}){
    const { tarefa, tempo } = props;
    return(
        <li className='item'>
        <h3>{tarefa}</h3>
        <span>{tempo}</span>
        </li>
    )
}