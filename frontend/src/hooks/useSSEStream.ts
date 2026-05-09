"use client";

import { useEffect, useState } from "react";

export function useSSEStream(url: string) {

  const [messages, setMessages] = useState<string[]>([]);

  useEffect(() => {

    const eventSource = new EventSource(url);

    eventSource.onmessage = (event) => {

      try {

        const parsed = JSON.parse(event.data);

        if (parsed.type === "token") {

          setMessages((prev) => [
            ...prev,
            parsed.delta
          ]);

        }

      } catch (err) {

        console.error("SSE Parse Error:", err);

      }

    };

   eventSource.onerror = () => {

  eventSource.close();

}; 

    return () => {

      eventSource.close();

    };

  }, [url]);

  return messages;
}