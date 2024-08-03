import React from 'react';
import style from './Botao.module.scss';

interface BotaoProps {
    children: React.ReactNode; 
}

class Botao extends React.Component<BotaoProps> {
    render() {
     return  (
            <button className={style.botao}>
             {this.props.children}
            </button>
        );
    }
}
export default Botao;