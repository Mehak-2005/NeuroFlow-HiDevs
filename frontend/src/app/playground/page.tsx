"use client";

import { useState } from "react";
import { useSSEStream } from "@/hooks/useSSEStream";

export default function PlaygroundPage() {

  const [query, setQuery] = useState("");
  const [compareMode, setCompareMode] = useState(false);
  const [openDrawer, setOpenDrawer] = useState(false);

  const runId = "abc-123";

  const messages = useSSEStream(
    `http://127.0.0.1:8000/query/${runId}/stream`
  );

  return (
    <div className="p-8 space-y-6 min-h-screen bg-black text-white">

      {/* HEADER */}

      <h1 className="text-4xl font-bold">
        Query Playground
      </h1>

      {/* PIPELINE SELECTOR */}

      <select className="border border-gray-700 bg-zinc-900 p-3 rounded w-full">

        <option>Pipeline A (0.87)</option>
        <option>Pipeline B (0.81)</option>

      </select>

      {/* QUERY INPUT */}

      <textarea
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="border border-gray-700 bg-zinc-900 p-4 rounded w-full h-40"
        placeholder="Ask a question..."
      />

      {/* CHARACTER COUNTER */}

      <div className="text-sm text-gray-400">
        Characters: {query.length}
      </div>

      {/* COMPARE MODE */}

      <label className="flex items-center gap-3 text-lg">

        <input
          type="checkbox"
          checked={compareMode}
          onChange={() => setCompareMode(!compareMode)}
        />

        Compare Mode

      </label>

      {/* SINGLE MODE */}

      {!compareMode ? (

        <div className="border border-green-500 rounded p-6 bg-black text-green-400 min-h-[250px]">

          <h2 className="font-bold text-2xl mb-4">
            Streaming Response
          </h2>

          {/* STREAMING TOKENS */}

          <div className="space-y-1">

            {messages.map((msg, idx) => (
              <div key={idx}>{msg}</div>
            ))}

          </div>

          {/* CITATIONS */}

          <div className="flex gap-3 mt-6">

            <button className="bg-blue-500 hover:bg-blue-600 px-4 py-2 rounded">
              Source 1
            </button>

            <button className="bg-blue-500 hover:bg-blue-600 px-4 py-2 rounded">
              Source 2
            </button>

          </div>

          {/* DRAWER BUTTON */}

          <button
            onClick={() => setOpenDrawer(true)}
            className="bg-purple-500 hover:bg-purple-600 px-4 py-2 rounded mt-6"
          >
            Open Citation Drawer
          </button>

          {/* FEEDBACK BUTTONS */}

          <div className="flex gap-4 mt-6">

            <button className="bg-green-500 hover:bg-green-600 px-5 py-2 rounded text-black font-bold">
              👍
            </button>

            <button className="bg-red-500 hover:bg-red-600 px-5 py-2 rounded text-black font-bold">
              👎
            </button>

          </div>

          {/* EVALUATION GAUGES */}

          <div className="space-y-5 mt-8">

            <div>

              <p className="mb-2">
                Faithfulness
              </p>

              <div className="w-full bg-gray-700 rounded h-4">

                <div className="bg-green-500 h-4 rounded w-[90%] animate-pulse"></div>

              </div>

            </div>

            <div>

              <p className="mb-2">
                Answer Relevance
              </p>

              <div className="w-full bg-gray-700 rounded h-4">

                <div className="bg-blue-500 h-4 rounded w-[80%] animate-pulse"></div>

              </div>

            </div>

            <div>

              <p className="mb-2">
                Context Precision
              </p>

              <div className="w-full bg-gray-700 rounded h-4">

                <div className="bg-yellow-500 h-4 rounded w-[75%] animate-pulse"></div>

              </div>

            </div>

            <div>

              <p className="mb-2">
                Context Recall
              </p>

              <div className="w-full bg-gray-700 rounded h-4">

                <div className="bg-pink-500 h-4 rounded w-[85%] animate-pulse"></div>

              </div>

            </div>

          </div>

        </div>

      ) : (

        /* COMPARE MODE */

        <div className="grid grid-cols-2 gap-6">

          {/* PIPELINE A */}

          <div className="border border-green-500 rounded p-4 bg-black text-green-400 min-h-[250px]">

            <h2 className="font-bold text-xl mb-4">
              Pipeline A
            </h2>

            {messages.map((msg, idx) => (
              <div key={idx}>{msg}</div>
            ))}

          </div>

          {/* PIPELINE B */}

          <div className="border border-blue-500 rounded p-4 bg-black text-blue-400 min-h-[250px]">

            <h2 className="font-bold text-xl mb-4">
              Pipeline B
            </h2>

            {messages.map((msg, idx) => (
              <div key={idx}>{msg}</div>
            ))}

          </div>

        </div>

      )}

      {/* SIDE DRAWER */}

      {openDrawer && (

        <div className="fixed right-0 top-0 w-96 h-full bg-zinc-900 border-l border-gray-700 p-6 z-50 shadow-2xl">

          <button
            onClick={() => setOpenDrawer(false)}
            className="bg-red-500 hover:bg-red-600 px-4 py-2 rounded mb-6"
          >
            Close
          </button>

          <h2 className="text-2xl font-bold mb-4">
            Citation Details
          </h2>

          <p className="text-gray-300 leading-7">
            Artificial intelligence is the simulation of human intelligence
            processes by machines, especially computer systems.
          </p>

          <div className="mt-6 space-y-2 text-sm text-gray-400">

            <p>📄 Document: sample.pdf</p>

            <p>📑 Page: 1</p>

            <p>🧩 Chunk ID: chunk-001</p>

          </div>

        </div>

      )}

    </div>
  );
}