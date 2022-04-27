import './styles/App.css';
import Home from './pages/Home';
import { Switch, Route } from 'react-router-dom';
import Gmail from './pages/Gmail';
import Images from './pages/Images';
import TestPage from './components/TestPage';
import CorrectedPage from './components/CorrectedPage';

function App() {
  return (
    <>
      <Switch>
        <Route path='/' exact component={Home} />
        <Route path='/gmail' component={Gmail} />
        <Route path='/images' component={Images} />
        <Route path='/test_page' component={TestPage} />
        <Route path='/corrected_page' component={CorrectedPage} />
      </Switch>
    </>
  );
}

export default App;
