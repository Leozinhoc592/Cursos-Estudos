import styled from 'styled-components'
import logo from '../../imagens/logo.svg'


const LogoEscrito = styled.div`
  display: flex;
  font-size: 30px;
`
const LogoImg = styled.img`
  margin-right:  10px;
`

function Logo() {
    return (
        <LogoEscrito>
          <LogoImg
          src={logo}
           alt='logo'
            />
          <p><strong>Alura</strong>Books</p>
        </LogoEscrito>
    )

}

export default Logo