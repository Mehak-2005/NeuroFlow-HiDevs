"use client";

import { useState } from "react";

export default function DocumentsPage() {

  const [documents] = useState([
    {
      id: 1,
      filename: "sample.pdf",
      status: "Processing",
      chunks: 25,
      uploaded: "2 mins ago",
    },
    {
      id: 2,
      filename: "research.docx",
      status: "Completed",
      chunks: 40,
      uploaded: "10 mins ago",
    },
  ]);

  return (
    <div className="p-8 min-h-screen bg-black text-white">

      <h1 className="text-4xl font-bold mb-10">
        Documents
      </h1>

      {/* Upload Zone */}

      <div className="border-2 border-dashed border-blue-500 rounded-lg p-16 text-center mb-10">

        <p className="text-2xl mb-4">
          Drag and drop files here
        </p>

        <input
          type="file"
          multiple
          className="mt-4"
        />

      </div>

      {/* Documents Table */}

      <table className="w-full border border-gray-700">

        <thead className="bg-zinc-900">

          <tr>

            <th className="border border-gray-700 p-3">
              Filename
            </th>

            <th className="border border-gray-700 p-3">
              Status
            </th>

            <th className="border border-gray-700 p-3">
              Chunks
            </th>

            <th className="border border-gray-700 p-3">
              Uploaded
            </th>

            <th className="border border-gray-700 p-3">
              Similarity Search
            </th>

          </tr>

        </thead>

        <tbody>

          {documents.map((doc) => (

            <tr key={doc.id}>

              <td className="border border-gray-700 p-3">
                📄 {doc.filename}
              </td>

              <td className="border border-gray-700 p-3">

                {doc.status === "Processing" ? (

                  <div className="flex items-center gap-2 text-blue-400">

                    <div className="w-3 h-3 bg-blue-500 rounded-full animate-pulse"></div>

                    Processing

                  </div>

                ) : (

                  <span className="text-green-400">
                    Completed
                  </span>

                )}

              </td>

              <td className="border border-gray-700 p-3">
                {doc.chunks}
              </td>

              <td className="border border-gray-700 p-3">
                {doc.uploaded}
              </td>

              <td className="border border-gray-700 p-3">

                <button className="bg-purple-500 hover:bg-purple-600 px-4 py-2 rounded">

                  Find Similar Chunks

                </button>

              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}