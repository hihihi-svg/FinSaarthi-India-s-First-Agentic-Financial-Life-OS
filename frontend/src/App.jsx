import React, { useState } from 'react';
import { 
  TrendingUp, 
  ShieldCheck, 
  Zap, 
  Users, 
  PieChart as PieChartIcon, 
  LayoutDashboard, 
  FileText, 
  Calculator, 
  Settings,
  ChevronRight,
  Menu,
  X
} from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import { queryAgent } from './api/client';

const App = () => {
  const [activeTab, setActiveTab] = useState('home');
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [loading, setLoading] = useState(false);
  const [apiResult, setApiResult] = useState(null);

  const handleQuery = async (queryType) => {
    setLoading(true);
    try {
      const profile = {
        gross_salary: 1500000,
        deductions_80c: 150000,
        hra: 50000,
        nps: 50000,
        medical: 25000,
        name: "Investor"
      };
      const result = await queryAgent(`Tell me about ${queryType}`, profile);
      setApiResult(result);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const features = [
    { 
      id: 'portfolio',
      title: 'MF Portfolio X-Ray', 
      desc: 'Instant analysis of your CAMS/KFintech statements.', 
      icon: <PieChartIcon className="w-6 h-6 text-blue-400" />,
      color: 'blue'
    },
    { 
      id: 'fire',
      title: 'FIRE Path Planner', 
      desc: 'Accurate goal-based SIP roadmap across generations.', 
      icon: <TrendingUp className="w-6 h-6 text-purple-400" />,
      color: 'purple'
    },
    { 
      id: 'tax',
      title: 'Tax Wizard', 
      desc: 'Optimize your tax regime and find missed deductions.', 
      icon: <FileText className="w-6 h-6 text-pink-400" />,
      color: 'pink'
    },
    { 
      id: 'couple',
      title: "Couple's Money Planner", 
      desc: 'Dual-income optimization for household efficiency.', 
      icon: <Users className="w-6 h-6 text-orange-400" />,
      color: 'orange'
    }
  ];

  const LandingPage = () => (
    <div className="animate-fade-in">
      <header className="flex justify-between items-center mb-16">
        <div className="flex items-center gap-2">
          <div className="w-10 h-10 bg-blue-600 rounded-xl flex items-center justify-center shadow-lg">
            <ShieldCheck className="text-white w-6 h-6" />
          </div>
          <span className="text-2xl font-bold tracking-tight">Fin<span className="text-blue-500">Saarthi</span></span>
        </div>
        <nav className="hidden md:flex gap-8 items-center font-medium text-slate-400">
          <a href="#" className="hover:text-white transition-colors">Features</a>
          <a href="#" className="hover:text-white transition-colors">Safety</a>
          <a href="#" className="hover:text-white transition-colors">About</a>
          <button onClick={() => setActiveTab('dashboard')} className="ml-4">Get Started</button>
        </nav>
      </header>

      <main className="text-center md:text-left max-w-4xl mx-auto py-20">
        <motion.h1 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-5xl md:text-7xl font-extrabold mb-6 leading-tight"
        >
          India's First <span className="gradient-text">Agentic Financial Life OS</span>
        </motion.h1>
        <motion.p 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="text-xl text-slate-400 mb-10 max-w-2xl leading-relaxed"
        >
          FinSaarthi acts as your personal AI-powered CFO. From mutual fund x-rays to couple's tax optimization, it transforms raw data into actionable financial roadmaps.
        </motion.p>
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="flex flex-col sm:flex-row gap-4"
        >
          <button onClick={() => setActiveTab('dashboard')} className="text-lg px-8 py-4 flex items-center justify-center gap-2 group">
            Launch Your CFO <ChevronRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
          </button>
          <button className="bg-transparent border border-white/20 hover:bg-white/5 text-lg px-8 py-4">
            Watch Demo
          </button>
        </motion.div>

        <div className="grid-layout mt-32">
          {features.map((f, i) => (
            <motion.div 
              key={f.title}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.3 + (i * 0.1) }}
              className="glass-card flex flex-col items-start gap-4"
            >
              <div className={`p-3 rounded-xl bg-${f.color}-500/10 mb-2`}>
                {f.icon}
              </div>
              <h3 className="text-xl font-bold">{f.title}</h3>
              <p className="text-slate-400 text-sm">{f.desc}</p>
            </motion.div>
          ))}
        </div>
      </main>
    </div>
  );

  const Dashboard = () => (
    <div className="flex h-screen bg-[#0f172a] text-white -m-8 overflow-hidden">
      {/* Sidebar */}
      <aside className="w-64 border-r border-white/10 p-6 flex flex-col gap-8">
        <div className="flex items-center gap-2 mb-4">
          <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center">
            <ShieldCheck className="text-white w-5 h-5" />
          </div>
          <span className="text-xl font-bold tracking-tight">FinSaarthi</span>
        </div>
        
        <nav className="flex flex-col gap-2">
          <NavItem icon={<LayoutDashboard size={20} />} label="Overview" active={true} />
          <div className="text-xs font-semibold text-slate-500 uppercase tracking-widest mt-6 mb-2">Agents</div>
          {features.map(f => (
            <NavItem key={f.id} icon={f.icon} label={f.title} />
          ))}
          <div className="mt-auto pt-8">
            <NavItem icon={<Settings size={20} />} label="Settings" />
          </div>
        </nav>
      </aside>

      {/* Main Content */}
      <main className="flex-1 p-10 overflow-auto">
        <header className="flex justify-between items-center mb-10">
          <div>
            <h2 className="text-3xl font-bold">Welcome back, <span className="text-blue-400">Investor</span></h2>
            <p className="text-slate-400">Your financial life is fully optimized.</p>
          </div>
          <div className="flex gap-4">
            <button className="bg-white/5 border border-white/10 px-4 py-2 text-sm">Feedback</button>
            <button 
              onClick={() => handleQuery('tax')} 
              disabled={loading}
              className="px-4 py-2 text-sm"
            >
              {loading ? 'Analyzing...' : 'Run Tax Optimizer'}
            </button>
          </div>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <StatCard label="Net Worth" value="₹42,50,000" change="+12.5%" />
          <StatCard label="Annual Savings" value="₹1,24,000" change="+₹18k" />
          <StatCard label="Portfolio XIRR" value="14.8%" change="+2.1%" />
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div className="glass-card min-h-[300px]">
            <h4 className="text-lg font-bold mb-4">Wealth Projection</h4>
            <div className="h-48 bg-white/5 rounded-xl border border-dashed border-white/20 flex items-center justify-center text-slate-500 text-sm">
              Chart implementation coming soon...
            </div>
          </div>
          <div className="glass-card min-h-[300px]">
            <h4 className="text-lg font-bold mb-4">Agent Logic Hub</h4>
            <div className="space-y-4">
              {apiResult ? (
                <div className="animate-fade-in p-4 bg-blue-600/10 rounded-xl border border-blue-500/20">
                    <p className="text-blue-400 font-bold mb-2">Orchestrator Result:</p>
                    <p className="text-sm leading-relaxed">{apiResult.final_response}</p>
                </div>
              ) : (
                <>
                  <LogItem time="09:42" text="Portfolio Agent: Ready for analysis." />
                  <LogItem time="09:40" text="Tax Wizard: Awaiting input..." color="pink" />
                  <LogItem time="09:38" text="Orchestrator: System online." color="purple" />
                </>
              )}
            </div>
          </div>
        </div>
        
        <div className="mt-8 flex justify-center">
            <button onClick={() => setActiveTab('home')} className="bg-transparent text-slate-500 hover:text-white">← Back to Home</button>
        </div>
      </main>
    </div>
  );

  return (
    <div className="min-h-screen">
      {activeTab === 'home' ? <LandingPage /> : <Dashboard />}
    </div>
  );
};

const NavItem = ({ icon, label, active = false }) => (
  <div className={`flex items-center gap-3 p-3 rounded-xl cursor-pointer transition-all ${active ? 'bg-blue-600/20 text-blue-400 border border-blue-500/20' : 'hover:bg-white/5 text-slate-400'}`}>
    {icon}
    <span className="font-medium text-sm">{label}</span>
  </div>
);

const StatCard = ({ label, value, change }) => (
  <div className="glass-card p-6 flex flex-col gap-2">
    <span className="text-slate-400 text-xs font-semibold uppercase tracking-wider">{label}</span>
    <div className="flex items-end justify-between">
      <span className="text-3xl font-bold">{value}</span>
      <span className="text-green-400 text-sm font-medium">{change}</span>
    </div>
  </div>
);

const LogItem = ({ time, text, color = 'blue' }) => (
  <div className="flex gap-3 text-sm border-l-2 border-slate-700 pl-4 py-1">
    <span className="text-slate-500 font-mono">{time}</span>
    <span className={`text-${color}-400`}>{text}</span>
  </div>
);

export default App;
