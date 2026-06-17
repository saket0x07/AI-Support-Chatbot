import ChatInterface from "../components/ChatInterface";

export default function Home() {
  return (
    <main className="min-h-screen bg-slate-950 flex flex-col items-center justify-center p-4 sm:p-24">
      <div className="z-10 max-w-5xl w-full items-center justify-between text-sm flex flex-col gap-8">
        <div className="text-center space-y-2">
          <h1 className="text-3xl font-bold tracking-tight text-white sm:text-4xl bg-gradient-to-r from-sky-400 to-blue-500 bg-clip-text text-transparent">
            CloudFlow AI Customer Support
          </h1>
          <p className="text-slate-400 max-w-md mx-auto">
            Powered by Retrieval-Augmented Generation (RAG) and real-time intent & sentiment tagging.
          </p>
        </div>
        <div className="w-full">
          <ChatInterface />
        </div>
      </div>
    </main>
  );
}

