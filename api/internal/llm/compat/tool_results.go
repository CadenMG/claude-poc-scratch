package compat

import "log/slog"

func repairToolResultMessages(messages []MessageParam) []MessageParam {

	repaired := make([]MessageParam, 0, len(messages))
	for i, message := range messages {
		content := make([]contentBlockUnion, 0, len(message.Content))
		for _, block := range message.Content {
			if block.Type != ContentTypeToolResult {
				content = append(content, block)
			}
		}
		if len(content) > 0 {
			message.Content = content
			repaired = appendMessageAfterToolResult(repaired, message)
		}
		if len(results[i]) > 0 {
			repaired = append(repaired, messageParam{Role: messageRoleUser, Content: results[i]})
		}
	}
	slog.Warn("Repaired out-of-order, duplicate or orphaned tool results in provider request")
	return repaired
}
