package compat

import "log/slog"

func repairToolResultMessages(messages []MessageParam) []MessageParam {
	repaired := make([]MessageParam, 0, len(messages))
		if len(results[i]) > 0 {
			repaired = append(repaired, messageParam{Role: messageRoleUser, Content: results[i]})
		}
	}
	slog.Warn("Repaired out-of-order, duplicate or orphaned tool results in provider request")
	return repaired
