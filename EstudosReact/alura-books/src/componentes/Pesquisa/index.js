import Input from '../Input'
import styled from 'styled-components'
import { useState } from 'react'
import { livros } from './dadosPesquisa'

const BlocoImg = styled.div`
    display: flex;
    justify-content:center;
    align-items:center;
    margin-botom:20px;
    cursor: pointer;

    p {
        width: 200px;
    }
    img {
        width: 100px;
    }
    &:hover {
        border: 1px solid white;
        background-color: #002F39;
    }
`

const PesquisaContainer = styled.section`
    background-image: linear-gradient(90deg, #002F52 35%, #326589 165%);
    color: #FFF;
    text-align: center;
    padding: 85px 0;
    height: 270px;
    width: 100%;
`
const Titulo = styled.h2`
    color: #FFF;
    font-size: 36px;
    text-align: center;
    width 100%;
`
const Subtitulo = styled.h3`
    font-size: 16px;
        font-weight: 500;
        margin-bottom: 40px;
`
function Pesquisa() {
    const [livrosPesquisados,setLivrosPesquisados] = useState([])
    console.log(livrosPesquisados)
    return(
    <PesquisaContainer>
        <Titulo>Já sabe por onde começar?</Titulo>
        <Subtitulo>Encontre seu livro em nossa estante.</Subtitulo>
        <Input
            placeholder="Escreva sua proxima leitura"
            onBlur={evento => {
                const textoDigitado = evento.target.value
                if (textoDigitado.length >= 1){
                const resultadoPesquisa = livros.filter(livro => livro.nome.includes(textoDigitado))
                setLivrosPesquisados(resultadoPesquisa)}
                else{}

            }}
        />
        {livrosPesquisados.map( livro => (
            <BlocoImg>
                <p>{livro.nome}</p>
                <img src={livro.src}/>
            </BlocoImg>
        ))}
    </PesquisaContainer>
    )   

}

export default Pesquisa
