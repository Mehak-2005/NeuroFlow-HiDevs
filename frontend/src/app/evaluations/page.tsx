"use client";

import { useSSEStream } from "@/hooks/useSSEStream";

export default function EvaluationsPage() {

  const messages = useSSEStream(
    "http://127.0.0.1:8000/evaluations/stream"
  );

  return (
    <div className="p-8">

      <h1 className="text-3xl font-bold mb-6">
        Evaluation Feed
      </h1>

      <div className="space-y-4">

        {messages.map((msg, idx) => (

          <div
            key={idx}
            className="border rounded p-4 bg-zinc-900"
          >

            <p className="font-bold">
              {msg}
            </p>

            <div className="mt-2 h-2 bg-green-500 rounded w-3/4"></div>

          </div>

        ))}

      </div>

    </div>
  );
}