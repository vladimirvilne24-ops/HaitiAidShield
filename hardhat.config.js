require("@nomicfoundation/hardhat-toolbox");

module.exports = {
  solidity: "0.8.20",
  networks: {
    amoy: {
      url: "https://rpc-amoy.polygon.technology",
      accounts: ["0x589cdee4bb39f6a8af3a0d49b0653eb5d1b324d38e3bbfdc789b7a61a1a424ef"]
    }
  }
};