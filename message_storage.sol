// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MessageStorage {
    struct Message {
        address user;
        uint256 guildId;
        uint256 channelId;
        string content;
        uint256 timestamp;
    }

    Message[] public messages;

    function addMessage(address _user, uint256 _guildId, uint256 _channelId, string memory _content) public {
        Message memory newMessage = Message({
            user: _user,
            guildId: _guildId,
            channelId: _channelId,
            content: _content,
            timestamp: block.timestamp
        });

        messages.push(newMessage);
    }

    function getMessageCount() public view returns (uint256) {
        return messages.length;
    }
}
