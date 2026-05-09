"use client";

import Editor from "@monaco-editor/react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip
} from "recharts";

export default function PipelinesPage() {

  return (
    <div className="p-8 space-y-6">

      <h1 className="text-3xl font-bold">
        Pipeline Manager
      </h1>

      <div className="border rounded p-4">

        <h2 className="text-xl font-bold mb-4">
          Create Pipeline
        </h2>

        <Editor
          height="400px"
          defaultLanguage="json"
          defaultValue={`{
  "name": "legal-pipeline",
  "chunk_size": 400
}`}
        />

      </div>

    </div>
  );
}