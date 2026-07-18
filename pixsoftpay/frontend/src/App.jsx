import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Dashboard from './components/Dashboard';
import CreatePayment from './components/CreatePayment';
import PaymentPage from './components/PaymentPage';
import History from './components/History';

export default function App() {
  return (
    <>
      <Navbar />
      <div className="container">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/create" element={<CreatePayment />} />
          <Route path="/pay/:reference" element={<PaymentPage />} />
          <Route path="/history" element={<History />} />
        </Routes>
      </div>
    </>
  );
}
