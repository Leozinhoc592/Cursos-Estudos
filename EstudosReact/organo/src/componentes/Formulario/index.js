import './Formulario.css';
import CampoTexto from '../CampoTexto/CampoTexto';
import ListaSuspensa from '../ListaSuspensa';
import Botao from '../Botao';
const Formulario = () => {
    
    const times = [
        'Progamação',
        'Front-End',
        'Data Science',
        'UX e Design',
        'Mobile',
        'Inovação e Gestão'
    ]

    const aoSalvar = () => {
        console.log('Form foi submetido')
    }

    return (
        <section className='formulario'>
            <form onSubmit={aoSalvar}>
            <h2>Preencha os dados para criar o card do colaborador</h2>
            <CampoTexto label="Nome" placeholder="Digite seu nome"/>
            <CampoTexto label="Cargo" placeholder="Digite seu cargo"/>
            <CampoTexto label="Imagem" placeholder="Digite o endereço da imagem"/> 
            <ListaSuspensa itens={times} label="Time"/>
            <Botao>
                Criar Card
            </Botao>
            </form>
        </section>
    )
}

export default Formulario;