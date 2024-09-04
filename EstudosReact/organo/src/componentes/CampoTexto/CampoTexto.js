import './CampoTexto.css'
import {useState} from 'react'
function CampoTexto(props) {

    const [valor, setValor] = useState('Paulo Silveira')
    const aoDigitado = (evento) => {
        setValor(evento.target.value)
    }



    return(
    <div className='campo-texto'>
        <label>{props.label}</label>
        <input value={valor} onChange={aoDigitado} required={props.obrigatorio} placeholder= {props.placeholder}/>
        
    </div>
    )
}

export default CampoTexto